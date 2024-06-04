const wrapper = document.querySelector('.wrapper');
const btnPopup = document.querySelector('.btnLogin-popup');
const icon_close = document.querySelector('.icon-close');
const blury = document.querySelector('.paragraph');

btnPopup.addEventListener('click', () => {
    wrapper.classList.toggle('active-popup');
    blury.classList.toggle('blur');
});

icon_close.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup')
    blury.classList.remove('blur');
});

