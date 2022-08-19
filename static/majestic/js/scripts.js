const   menu_btn = document.getElementById('menu-btn'),
        menu = document.getElementById('header-nav');


menu_btn.addEventListener('click', function(e) {
    if (menu_btn.hasAttribute('is_active')) {
        document.body.removeAttribute('is_active', '');
        menu_btn.removeAttribute('is_active', '');
        menu.removeAttribute('is_active', '');
    } else {
        document.body.setAttribute('is_active', '');
        menu_btn.setAttribute('is_active', '');
        menu.setAttribute('is_active', '');
    }
});