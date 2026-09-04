const newsData = [
  {
    id: 1,
    title: "Ferminal now available on Arch User Repository",
    link: "https://aur.archlinux.org/packages/ferminal",
    date: "2026-07-17",
    content: `
      <p>Ferminal v1.3.3 is now available on the Arch User Repository (AUR). You can install it using your preferred AUR helper. Example:</p>
      <div class="arch-code-block">
        <code>yay -S ferminal</code>
      </div>
      <p><strong>Don't forget to check PKGBUILD on <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=ferminal" target="_blank" rel="noopener noreferrer">AUR</a>!</strong></p>
    `
  },
  {
    id: 2,
    title: "ferminal-aur-package &amp; man page documentation update",
    link: "docs/installation/",
    date: "2026-08-01",
    content: `
      <p>Previously, installation instructions lacked official Arch Linux User Repository (AUR) guidelines and manual page details for <code class="arch-code">ferminal.1</code>. To install and access full offline terminal documentation, you can use one of the following methods:</p>
      <ul class="arch-news-list-bullets">
        <li>Install <code class="arch-code">ferminal</code> package directly via AUR helper before upgrading the system.</li>
        <li>Run <code class="arch-code">man ferminal</code> as user for quick offline command lookup.</li>
        <li>Instruct <code class="arch-code">pacman</code> or AUR helper once to overwrite existing files:</li>
      </ul>
      <div class="arch-code-block">
        <code>pacman -Syu --overwrite '/usr/share/man/man1/ferminal.1.gz'</code>
      </div>
    `
  },
  {
    id: 3,
    title: "Port Package build for FreeBSD",
    link: "docs/installation/",
    date: "2026-08-04",
    content: `
      <p>We have updated the installation method for freebsd system via .pkg file. User just need to install with:</p>
      <div class="arch-code-block">
        <code>pkg install ferminal-1.3.3.pkg</code>
      </div>
      <p>
        This is ferminal v1.3.3 package for freebsd system. You can also check the <a href="https://github.com/RangS-1/Ferminal/releases/tag/v1.3.3" target="_blank" rel="noopener noreferrer">GitHub releases page</a> for more information.
      </p>
    `
  }
];

function renderNewsList() {
  const newsListContainers = document.querySelectorAll('.arch-news-list');
  if (!newsListContainers || newsListContainers.length === 0) return;

  // Sort news by highest ID first (newest to oldest)
  const sortedNews = [...newsData].sort((a, b) => b.id - a.id);

  // Determine path prefix for internal links based on page location
  const isNewsPage = window.location.pathname.includes('/news/');
  const pathPrefix = isNewsPage ? '../' : '';

  const htmlContent = sortedNews.map(item => {
    let href = item.link;
    let targetAttr = '';

    const isExternal = href.startsWith('http://') || href.startsWith('https://');
    if (isExternal) {
      targetAttr = 'target="_blank" rel="noopener noreferrer"';
    } else {
      href = pathPrefix + href;
    }

    return `
      <article class="arch-news-item">
        <div class="arch-news-item-header">
          <h3 class="arch-news-item-title">
            <a href="${href}" ${targetAttr}>${item.title}</a>
          </h3>
          <span class="arch-news-item-date">${item.date}</span>
        </div>
        <div class="arch-news-item-body">
          ${item.content}
        </div>
      </article>
    `;
  }).join('');

  newsListContainers.forEach(container => {
    container.innerHTML = htmlContent;
  });
}

document.addEventListener('DOMContentLoaded', renderNewsList);
