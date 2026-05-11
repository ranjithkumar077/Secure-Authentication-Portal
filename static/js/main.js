// Form Validation Logic
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                // Custom password match validation for registration form
                if (form.id === 'registerForm') {
                    var password = document.getElementById('password');
                    var confirm = document.getElementById('confirm_password');
                    var mismatchMsg = document.getElementById('passwordMismatch');
                    
                    if (password.value !== confirm.value) {
                        confirm.setCustomValidity("Passwords do not match");
                        mismatchMsg.classList.remove('d-none');
                        event.preventDefault();
                        event.stopPropagation();
                    } else {
                        confirm.setCustomValidity("");
                        mismatchMsg.classList.add('d-none');
                    }
                }

                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })

    // Auto dismiss alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
})()
