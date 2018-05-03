$(document).ready(function(){
    $("#about-btn").click(function(event){
        alert("你点了！")
    });

    $(".ouch").click(function(event){
        alert("你点了ouch")
    });
    $("p").hover(
        function()
        {
            $(this).css('color','red');
        },
        function()
        {
            $(this).css('color','blue');
        },
    );

    $('#about-btn').click(
        function(event)
        {
            msgstr = $("#msg").html()
            msgstr = msgstr + "ooo"
            $("#msg").html(msgstr)
        }
    );
});
