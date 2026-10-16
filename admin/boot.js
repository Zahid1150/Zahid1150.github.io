window.CMS_MANUAL_INIT = true;
(async () => {
  const status = document.getElementById('status');
  try {
    const responses = await Promise.all([fetch('auth.json'), fetch('config.json')]);
    if (responses.some(r => !r.ok)) throw new Error('Configuration unavailable');
    const [auth, config] = await Promise.all(responses.map(r => r.json()));
    if (!auth.enabled || !auth.site_domain) {
      status.textContent = 'Editor prepared · Secure sign-in is not connected yet.';
      document.getElementById('setup-help').hidden = false;
      return;
    }
    config.site_domain = auth.site_domain;
    config.backend.base_url = auth.base_url;
    config.backend.auth_endpoint = auth.auth_endpoint;
    status.textContent = 'Sign in with the GitHub account that has editing access to this repository.';
    const launch = document.getElementById('launch');
    launch.hidden = false;
    launch.addEventListener('click', () => {
      launch.disabled = true;
      const script = document.createElement('script');
      script.src = 'https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js';
      script.onload = () => { document.getElementById('setup').hidden = true; window.CMS.init({config}); };
      script.onerror = () => { status.textContent = 'The editor could not load. Check your connection and try again.'; launch.disabled = false; };
      document.head.append(script);
    });
  } catch (error) {
    status.textContent = 'The editor configuration could not load. Open this page through the website server.';
  }
})();
