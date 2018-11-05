$(function () {

     $('.type-item li').mouseover(function () {
        $(this).css({'color':'darkred','font-weight':'bold'}).siblings().css({'color':'#444','font-weight':'normal'});
		$('.f_l_c_content div').eq($(this).index()).show().siblings().hide();
		indexs = $(this).index();
		if(indexs >= $('.floor_liquor h1 ul li').length - 1){
			indexs = $('.floor_liquor h1 ul li').length - 2;
			$('.floor_liquor h1 ul li').eq(indexs).css({'color':'darkred','font-weight':'bold'}).siblings().css({'color':'#444','font-weight':'normal'});
		}
		$('.floor_liquor h1 p').css('left',600 + indexs * width + "px")
         alert("执行了")
     })


})