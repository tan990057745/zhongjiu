$(function () {
    var strings = "";
    $('.testbutton').click(function () {
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

    count = 1;
    $(".changeCode").click(function () {
        count ++;
        $(".testcode").attr("src", "/verifycode/"+count +"/");
        // alert("被执行了")

    })
})