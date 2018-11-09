$(function(){

    $('#subButton').on('click', function () {
         // console.log('登录')

        temp1 = checkingAccount()
        temp2 = checkingPassword()
        if ( temp1 && temp2 ){
            $('.header_bottom_right form').submit()
        }
    })

    function checkingAccount() {
        // 数字、字母
        var reg = /^[A-Za-z0-9]+$/
        var accountInput = $('#account input')
        if (reg.test(accountInput.val())) {  // 符合
            $('#account i').html('')
            $('#account').removeClass('has-error').addClass('has-success')
            $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok')

            return true
        } else {    // 不符合
            $('#account i').html('账号由数字、字母组成')
            $('#account').removeClass('has-success').addClass('has-error')
            $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return false
        }
    }

    function checkingPassword() {
        // 数字
        var reg = /^[\d]{6,12}$/
        var passwordInput = $('#password input')
        if (reg.test(passwordInput.val())) {  // 符合
            $('#password i').html('')
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            return true
        } else {    // 不符合
            $('#password i').html('6~12位纯数字')
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return false
        }
    }



	// var arr2 = $.cookie("obj2") ? JSON.parse($.cookie("obj2")) : [];
	// if (arr2.length){
	// 	$('.inp1').val(arr2[0].name);
	// 	$("input:checkbox").prop("checked", arr2[0].flag);
	// }
	// var arr = $.cookie("obj") ? JSON.parse($.cookie("obj")) : [];
	// $('.bnt1').click(function(){
	// 	var arr1 = [];
	// 	for(var i = 0;i < arr.length; i++){
	// 		if(arr[i].name == $('.inp1').val() && arr[i].paw == $('.inp2').val()){
	// 			$('h1').css('display','none');
	// 			var obj2 = {};
	// 			obj2.name = $('.inp1').val();
	// 			obj2.paw = $('.inp2').val();
	// 			obj2.flag = $("input:checkbox").prop("checked");
	// 			arr1.push(obj2);
	// 			$.cookie("obj2", JSON.stringify(arr1), {expires:7, path:"/"});
	// 			window.location.href = "home_page.html";
	// 		}else{
	// 			$('h1').css('top','20px')
	// 			$('h1').html("用户名或密码错误");
	// 			$('h1').css('border','1px solid red').css('display','block').css('color','red');
	// 		}
	// 	}
	// })
})