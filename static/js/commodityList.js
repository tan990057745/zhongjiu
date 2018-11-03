$(function(){
	//头部下拉框
	$('.h_b_b_title').mouseenter(function(){
		$('.h_b_b_t_nav').show();
	})
	$('.h_b_b_title').mouseleave(function(){
		$('.h_b_b_t_nav').hide();
	})
	$.getJSON("json/commodityList.json",function(data){
		//遍历，取得ul
		for (var i=0; i < data.length; i++){
			var li = $("<li><img src = "+data[i].img+"/><h4>"+data[i].name+"</h4><p><i>"+data[i].price+"</i><span>"+data[i].comment+"</span></p></li>");
			$(".content_left_bottom ul").append(li);
		}
	})
	//给标签一个点击事件
	$('.ul2 li a').eq(0).css('background','red').css('color','white');
	$('.ul2 li a').click(function(e){
		e.preventDefault();
		$(this).css('background','red').css('color','white').parent().siblings().children('a').css('background','white').css('color','#666');
	})
	$.getJSON("json/commodityList.json",function(data){
		//遍历，取得ul
		for(var j = 0; j < 4; j++){
			for (var i = 0; i < data.length; i++){
				var li = $("<li><img src = "+data[i].img+"/><h4>"+data[i].name+"</h4><p><i>"+data[i].price+"</i><span>"+data[i].comment+"</span></p><button class='btn1'>加入购物车</button><button class='btn2'>收藏</button></li>");
				$(".content_right .shops ul").append(li);
			}
		}
	})
	//回到顶部
	$(window).scroll(function(){
		var top = $(window).scrollTop();
		if(top >= 800){
			$('.div').show();
		}else{
			$('.div').hide()
		}	
	})
	$('.div').click(function(){
		var top = $(window).scrollTop();
		var timer = setInterval(function(){
			top -= 300;
			console.log(top)
			if(top <= 0)
			{
				top = 0;
				$(window).scrollTop(top);
				clearInterval(timer);
			}
			$(window).scrollTop(top);
		},10);	
	})
	
})