//ul li a 高亮显示
$(function(){
	var nav = $(".nav li a");
	nav.click(function() {
		/* Act on the event */
		nav.removeClass('bd')
		$(this).addClass('bd');
		return false;
	});

})