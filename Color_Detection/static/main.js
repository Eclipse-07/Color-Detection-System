document.addEventListener('DOMContentLoaded', function () {
    const switchers = [...document.querySelectorAll('.switcher')]; 
    switchers.forEach(item => {
        item.addEventListener('click', function () {
            switchers.forEach(item => item.parentElement.classList.remove('is-active'));
            this.parentElement.classList.add('is-active');
        });
    }); 
    // Adding event listeners for the registration and login links
    const showRegister = document.getElementById('show-register');
    const showLogin = document.getElementById('show-login'); 
    showRegister.addEventListener('click', function () {
        document.querySelector('.switcher-register').click();
    }); 
    showLogin.addEventListener('click', function () {
        document.querySelector('.switcher-login').click();
    });
    const flashMessages = document.querySelectorAll('.alert');
    if (flashMessages.length > 0) {
      flashMessages.forEach((message) => {
        alert(message.textContent); // Trigger an alert with the flash message
      });}
});

  
  
  