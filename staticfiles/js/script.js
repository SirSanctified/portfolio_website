const btn = document.getElementById('menu-btn')
const nav = document.getElementsByClassName('navbar')

btn.addEventListener('click', () => {
    // btn.classList.toggle('open')
    nav.style.display = "flex"
    nav.style.transform = "translateX(0)"
})