// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${language}`;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
