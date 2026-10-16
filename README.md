# Md Zahidul Islam — personal website

## Website structure

Home, Research, Projects, Publications, Experience & Education, Community & Service, and Gallery. The mobile menu appears below 1201px. The academic CV remains a separate navigation button.

The homepage features physician scheduling, learning-based routing, supply-chain simulation, a brief background, selected honors, community involvement, and gallery/contact links. Detailed project and publication content has been preserved from the latest repository version.

## Editing and building

Editable content lives in `content/*.json`. These files control the homepage, navigation/document links, education, awards, community service, and gallery albums. Retained detailed research/project/experience page bodies are in `_site/pages/`.

Run from the repository root:

```sh
python _build/build.py
python _build/check_site.py
python _build/package_site.py
```

The public deployment folder is `dist/`. Source content, build scripts, and repository metadata are not included in it. Generated HTML at the repository root is also updated so the site can still be previewed directly.

For a local preview: `python -m http.server 8765`. Open `http://localhost:8765/`.

## GitHub Pages deployment

In repository Settings → Pages → Build and deployment, choose **GitHub Actions**. The included `pages.yml` workflow rebuilds, checks, packages, and publishes the site after a push to `main`. The website retains its `https://zahid1150.github.io` address.

## Admin editor — connection still required

Open `/admin/`. The Decap CMS configuration covers gallery uploads/albums/captions, homepage content, service activities, education, awards, navigation, and PDF links. The editor deliberately shows a setup status until authentication is connected; it is not a pretend upload form.

Follow `/admin/setup.html` and the official [Decap GitHub backend documentation](https://decapcms.org/docs/github-backend/) to configure a free-tier authentication provider. `admin/auth.json` contains only public provider settings. Keep OAuth client secrets in the provider, never in GitHub files. Set `enabled` only after the provider is configured, then verify login, draft saving, photo upload, publishing, and the GitHub deployment end to end.

An account with repository write permission is required. The default editorial workflow supports drafts and publishing. Git history provides rollback. Uploaded image files themselves are stored in the public repository, even when their gallery entry is not yet published.

Photos belong in gallery entries with image, alt text, caption, album, and optional date. No event photos were found in the supplied website assets, so the gallery begins with an honest empty state. Research figures are not used as substitutes for event photography. Images load lazily; upload web-sized JPEG/WebP photos (ideally under 2 MB). Automatic image compression is not implemented.

## Content provenance

Community roles and awards were checked against the supplied master CV and academic CV source. RUET student roles share the CV's grouped 2012–2016 period; exact per-role dates are not asserted. INFORMS Magna Cum Laude awards are explicitly chapter recognition. Existing resume/CV downloads were preserved. The homepage avoids the unverified night-shift “about half” reduction claim.

## Verification

Static checks cover local file references, anchors, unique IDs, one main landmark and one h1 per page, and content JSON. Browser checks cover all public pages at phone/tablet/desktop widths, image loading, horizontal overflow, mobile menu actions, reduced motion, editor setup status, and gallery filtering/enlargement using a temporary fixture. No sample gallery photos are published.

`_build/browser_check.cjs` needs Playwright and Microsoft Edge; set `NODE_PATH` to an installed Playwright package location when necessary. It is a local QA helper, not part of the deployment build.

Secure CMS login, uploads to the live repository, and live deployment require account access and cannot be certified by local tests.
