document.getElementById('password').addEventListener('input', function() {
    var icon = document.getElementById('password-icon').children[0];
    if (this.value.length > 0) {
        icon.setAttribute('name', 'lock-closed-sharp');
    } else {
        icon.setAttribute('name', 'lock-open-sharp');
    }
});
