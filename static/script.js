function toggleMenu(){
    const menu = document.querySelector(".menu-links");//targets an element on web page and use that element
    const icon = document.querySelector(".hamburger-icon");//targets an element on web page and use that element
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}
