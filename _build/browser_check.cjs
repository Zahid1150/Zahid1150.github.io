const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const mime = {'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.png':'image/png','.jpg':'image/jpeg','.pdf':'application/pdf'};
const server = http.createServer((req,res)=>{
  const name = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  let file=path.resolve(root,'.'+name);
  if(!file.startsWith(root+path.sep)&&file!==root){res.writeHead(403);res.end();return;}
  if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');
  if(!fs.existsSync(file)){res.writeHead(404);res.end();return;}
  res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base='http://127.0.0.1:'+server.address().port;
  const browser=await chromium.launch({headless:true,channel:'msedge'});
  const page=await browser.newPage();
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  const pages=fs.readdirSync(root).filter(f=>f.endsWith('.html')).concat(fs.readdirSync(path.join(root,'projects')).filter(f=>f.endsWith('.html')).map(f=>'projects/'+f));
  for(const width of [390,768,1440]){
    await page.setViewportSize({width,height:900});
    for(const file of pages){
      await page.goto(base+'/'+file);
      await page.locator('img').evaluateAll(imgs=>imgs.forEach(i=>i.loading='eager'));
      await page.waitForFunction(()=>Array.from(document.images).every(i=>i.complete));
      if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1))errors.push(`${file} horizontal overflow at ${width}`);
      const bad=await page.locator('img').evaluateAll(imgs=>imgs.filter(i=>!i.naturalWidth).map(i=>i.src));
      if(bad.length)errors.push(`${file} missing images: ${bad}`);
    }
  }
  await page.setViewportSize({width:390,height:844});
  await page.goto(base+'/index.html');
  const menu=page.locator('.menu-toggle');
  if(await page.locator('#site-nav').isVisible())errors.push('Mobile menu visible before opening');
  await menu.click();
  if(await menu.getAttribute('aria-expanded')!=='true')errors.push('Menu failed to open');
  await page.screenshot({path:path.join(root,'../website-mobile-menu.png')});
  await page.keyboard.press('Escape');
  if(await page.locator('#site-nav').isVisible())errors.push('Escape failed to close menu');
  await menu.click();await page.mouse.click(380,800);
  if(await page.locator('#site-nav').isVisible())errors.push('Outside click failed to close menu');
  await page.locator('img').evaluateAll(imgs=>imgs.forEach(i=>i.loading='eager'));
  await page.waitForFunction(()=>Array.from(document.images).every(i=>i.complete));
  await page.screenshot({path:path.join(root,'../website-mobile-preview.png'),fullPage:true});
  await page.setViewportSize({width:1440,height:1000});
  await page.goto(base+'/index.html');
  await page.locator('img').evaluateAll(imgs=>imgs.forEach(i=>i.loading='eager'));
  await page.waitForFunction(()=>Array.from(document.images).every(i=>i.complete));
  await page.screenshot({path:path.join(root,'../website-desktop-preview.png'),fullPage:true});
  await page.emulateMedia({colorScheme:'dark'});
  await page.screenshot({path:path.join(root,'../website-dark-preview.png'),fullPage:true});
  await page.emulateMedia({colorScheme:'light',reducedMotion:'reduce'});
  if(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior)!=='auto')errors.push('Reduced motion ignored');
  await page.goto(base+'/admin/');
  await page.getByText('Editor prepared · Secure sign-in is not connected yet.').waitFor();
  // Test gallery behavior using temporary HTML, without publishing invented photos.
  await page.goto(base+'/gallery.html');
  await page.evaluate(()=>{
    document.querySelector('main').insertAdjacentHTML('beforeend','<div class="gallery-filters"><button data-album="all" aria-pressed="true">All photos</button><button data-album="Test" aria-pressed="false">Test</button><button data-album="Other" aria-pressed="false">Other</button></div><figure class="gallery-item" data-album="Test"><button class="photo-open"><img src="images/photo.jpg" alt="Test portrait"></button><figcaption>Test caption</figcaption></figure><dialog class="photo-dialog"><button class="photo-close">Close</button><img alt=""><p></p></dialog>');
  });
  // Reload the script in an isolated scope so listeners bind to the test fixture.
  await page.addScriptTag({content:'{'+fs.readFileSync(path.join(root,'assets/site.js'),'utf8')+'}'});
  await page.getByRole('button',{name:'Other',exact:true}).click();
  if(await page.locator('.gallery-item').isVisible())errors.push('Gallery filter failed');
  await page.getByRole('button',{name:'All photos',exact:true}).click();
  await page.locator('.photo-open').click();
  if(!await page.locator('dialog').isVisible())errors.push('Gallery enlargement failed');
  await page.keyboard.press('Escape');
  if(await page.locator('dialog').isVisible())errors.push('Gallery Escape close failed');
  await browser.close();server.close();
  console.log(JSON.stringify({pages:pages.length,widths:[390,768,1440],errors},null,2));
  if(errors.length)process.exitCode=1;
})().catch(error=>{console.error(error);server.close();process.exit(1)});
