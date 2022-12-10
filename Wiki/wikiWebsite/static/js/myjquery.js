$(function() {
    $('#author-about').hide()

    $('.search-icon').on('click', function() {
      $(this).hide();
      $('.search-bar-list-item').fadeIn(200);
      $('.search-bar').focus();
      
      return false;
    });

    // Hide and show password text
    $('.bi-eye-fill').on('click', function() {
        $(this).hide();
        $('.bi-eye-slash-fill').show()
        $('#password').attr('type', 'text');
    });
    $('.bi-eye-slash-fill').on('click', function() {
        $(this).hide();
        $('.bi-eye-fill').show()
        $('#password').attr('type', 'password');
    });

    // Show author about
    $('.check-div').on('click', function() {
        if ($('#author').is(':checked')) {
            $('#author-about').show()
        } else {
            $('#author-about').hide()
        }
    });
    $('#author-txtarea').on('keyup', function() {
        $('.example-text').html($(this).val());
    });
});