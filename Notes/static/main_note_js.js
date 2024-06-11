const links = document.querySelectorAll('.semester-link');

// Add click event listener to each link
links.forEach(link => {
    link.addEventListener('click', function(event) {

        links.forEach(l => l.classList.remove('disabled'));
        if (!link.classList.contains('disabled')) {
            link.classList.add('disabled');
        }else {
            link.classList.remove('disabled');
        }
        const s_number = link.classList[1]; // Assuming the third class in the classList is the number
        const view_container = document.querySelector('.view-container.' + s_number);
        const view_containers= document.querySelectorAll('.view-container');  // Select view containers with the specified class
        view_containers.forEach(container => {container.classList.remove('selected');})
        view_container.classList.add('selected');
    });
});
