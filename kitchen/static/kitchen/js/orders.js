/**
 * Created by marc on 1/13/2015.
 */
$(function() {
    refresh_list();
});

window.setInterval(refresh_list, 5000);

function refresh_list() {
    $.get(refresh_url, function (data) {
            $('div#orders').html(data);
        });
}