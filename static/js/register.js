$(function(){
	// 刷新验证码
	count = 0;
	$(".changeCode").click(function () {
		count++
        $("#codePic").attr("src", "/verifycode/" + count +"/");
        // alert("被执行了")
    })


	// 免费获取校验码
	var strings = "";
    $('.getVerify').click(function () {
        strings = "";
        for (var i = 0; i < 4; i++) {
            var num = parseInt(Math.random() * 100) % 75 + 48;
            if ((num >= 48 && num <= 57) || (num >= 65 && num <= 90) || (num >= 97 && num <= 122)) {
                var str = String.fromCharCode(num);
                strings = strings.concat(str);
            } else {
                i--;
            }
        }
        alert(strings);
    })

	//比较校验码输入是否正确
	$('.inp3').change(function(){
		var checkCode = $('.inp3').val();
		if(checkCode.toLowerCase() == strings.toLowerCase()){
			alert("校验码输入正确");

		}else{
			alert("请输入正确的校验码");
		}
	})

	//比较两次密码是否输入一致
	$('.inp5').change(function () {
		if($('.inp4').val() == $('.inp5').val()){
			alert("两次密码输入正确");
		}else{
			alert("两次输入密码不一致");
		}
    })

})














