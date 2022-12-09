<?php
  /**
  * Requires the "PHP Email Form" library
  * The "PHP Email Form" library is available only in the pro version of the template
  * The library should be uploaded to: vendor/php-email-form/php-email-form.php
  * For more info and help: https://bootstrapmade.com/php-email-form/
  */

  // Replace contact@example.com with your real receiving email address

  // if( file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
  //   include( $php_email_form );
  // } else {
  //   die( 'Unable to load the "PHP Email Form" Library!');
  // }

  // $contact = new PHP_Email_Form;
  // $contact->ajax = true;
  
  // $contact->to = $_POST['email'];
  // $contact->from_name = 'Get Hitched';
  // $contact->from_email = 'get_hitched@gethitched.com';
  // $contact->subject = 'Reset Password';

  // // Uncomment below code if you want to use SMTP to send emails. You need to enter your correct SMTP credentials
  // /*
  // $contact->smtp = array(
  //   'host' => 'example.com',
  //   'username' => 'example',
  //   'password' => 'pass',
  //   'port' => '587'
  // );
  // */

  // $contact->add_message( 'Get Hitched', 'From');
  // $contact->add_message( 'get_hitched@gethitched.com', 'Email');
  // $contact->add_message( 'Click the link below to reset your password', 'Message', 10);

  // echo $contact->send();

    $msg = 'Please reset your password using the link below';
    mail($_POST['email'],"Reset Password",$msg);

?>
