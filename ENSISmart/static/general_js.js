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
    blury.classList.toggle('blur');
});

first_co.addEventListener('click', () => {
    wrapper.classList.add('notwrap');
    wrapper.classList.remove('active-popup');
    signup_wrap.classList.remove('notwrap');
    
    
});


btnPopup.addEventListener('click', () => {
    if (wrapper.classList.contains('active-popup') || !signup_wrap.classList.contains('notwrap')) {
        wrapper.classList.remove('active-popup');
        signup_wrap.classList.add('notwrap');
        blury.classList.toggle('blur');
    } else if (!wrapper.classList.contains('active-popup') && signup_wrap.classList.contains('notwrap')) {
        wrapper.classList.toggle('active-popup');
        blury.classList.toggle('blur');
    }
});


icon_close.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup')
    blury.classList.remove('blur');
});



document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        const formData = new FormData(form);
        fetch("{% url 'login' %}", {
            method: 'POST',
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('valid-address').style.display = 'block';
                document.getElementById('email-display').textContent = data.email;
                document.getElementById('error-messages').innerHTML = '';
            } else {
                document.getElementById('valid-address').style.display = 'none';
                document.getElementById('email-display').textContent = '';
                document.getElementById('error-messages').innerHTML = data.errors.join('<br>');
            }
        });
    });
});