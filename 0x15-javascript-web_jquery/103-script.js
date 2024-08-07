//  script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  function translate () {
    const language = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${language}`;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the keycode for the Enter key
      translate();
    }
  });
});
