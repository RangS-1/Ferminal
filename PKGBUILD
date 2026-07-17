pkgname=Ferminal
pkgver=1.3.3
pkgrel=1
pkgdesc="Custom Wrapper CLI to make your work faster"
arch=('any')
url="https://github.com/RangS-1/Ferminal"
license=('MIT')

depends=(
    'python'
    'python-requests'
    'python-colorama'
)

makedepends=(
    'python-build'
    'python-installer'
    'python-wheel'
)

source=("$pkgname-$pkgver.tar.gz::https://github.com/RangS-1/Ferminal/archive/refs/tags/v$pkgver.tar.gz")

sha256sums=('aa568bd073bad87dae20a007e9a58878dbea5ce42c85181bae639d60d856429b')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"

    python -m installer \
        --destdir="$pkgdir" \
        dist/*.whl

    install -Dm644 LICENSE \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}