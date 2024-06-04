const wrapper = document.querySelector('.wrapper');
const btnPopup = document.querySelector('.btnLogin-popup');
const icon_close = document.querySelector('.icon-close');
const icon_close_signup = document.querySelector('.icon-close.signup');
const signup_wrap = document.querySelector('.signup-wrap');
const blury = document.querySelector('.paragraph');
const first_co = document.querySelector('a.first-co');

icon_close_signup.addEventListener('click', () => {
    wrapper.classList.remove('notwrap');
    signup_wrap.classList.add('notwrap');
    blury.classList.remove('blur');
});

first_co.addEventListener('click', () => {
    wrapper.classList.add('notwrap');
    wrapper.classList.remove('active-popup');
    signup_wrap.classList.remove('notwrap');
    
});


btnPopup.addEventListener('click', () => {
    wrapper.classList.toggle('active-popup');
    blury.classList.toggle('blur');
});

icon_close.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup')
    blury.classList.remove('blur');
});



