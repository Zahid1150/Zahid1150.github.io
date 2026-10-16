"""Copy public files only into the deployment directory."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parent.parent
out=root/'dist'
out.mkdir(exist_ok=True)
for p in root.glob('*.html'):shutil.copy2(p,out/p.name)
for name in ['assets','images','docs','projects','admin']:
    shutil.copytree(root/name,out/name,dirs_exist_ok=True)
for name in ['Zahid_Islam_Resume.pdf','Zahid_Islam_Academic_CV.pdf','robots.txt','sitemap.xml']:
    shutil.copy2(root/name,out/name)
(out/'.nojekyll').touch()
print('Public website packaged in dist/.')
