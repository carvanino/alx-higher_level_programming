// $(function()
// {
//     $.ajax({
//         url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
//         success: function(data) {
//             $('DIV#character').text(data.name);
//         }
//     });
// });

$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
  });
});
