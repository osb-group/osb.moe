
// To enable Lightbox
// We also want to put in some of our own parameters within it, right?

$(document).on('click', '[data-toggle="lightbox"]', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});