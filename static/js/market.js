$(function () {

    // 点击设置cookie
    $('#brandBt li').click(function () {
        $.cookie('brandIndex', $(this).index(), {expires:3, path:'/'})
    })

    $('#placeBt li').click(function () {
        $.cookie('placeIndex', $(this).index(), {expires:3, path:'/'})
    })

    $('#priceBt li').click(function () {
        $.cookie('priceIndex', $(this).index(), {expires:3, path:'/'})
    })

    $('#suitBt li').click(function () {
        $.cookie('suitIndex', $(this).index(), {expires:3, path:'/'})
    })
    //
    $('#sortBt li').click(function () {
        $.cookie('sortIndex', $(this).index(), {expires:3, path:'/'})
    })
    // 点击样式
    // (1)
    brandIndex = $.cookie('brandIndex')
    if (brandIndex !=0){ // 已经有点击分类
        $('#brandBt li').eq(brandIndex).css('background', 'red').siblings().css('background', 'white');
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('#brandBt li').css('background', 'white');
    }
    //(2)
    placeIndex = $.cookie('placeIndex')
    if (placeIndex!=0){ // 已经有点击分类
        $('#placeBt li').eq(placeIndex).css('background', 'red').siblings().css('background', 'white');
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('#placeBt li').css('background', 'white');
    }
    // (3)
    priceIndex = $.cookie('priceIndex')
    if (priceIndex !=0){ // 已经有点击分类
        $('#priceBt li').eq(priceIndex).css('background', 'red').siblings().css('background', 'white');
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('#priceBt li').css('background', 'white');
    }
    //
    // (4)
    suitIndex = $.cookie('suitIndex')
    if (suitIndex !=0){ // 已经有点击分类
        $('#suitBt li').eq(suitIndex).css('background', 'red').siblings().css('background', 'white');
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('#suitBtkk li').css('background', 'white');
    }

    //(5)
    sortIndex = $.cookie('sortIndex')
    alert("执行了看看嘛")
    if (sortIndex !=0){ // 已经有点击分类
        $('#sortBt li').eq(sortIndex).children('a').css('background','red').parent().sibling().children('a').css('background', 'white');
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('#sortBt li').eq(1).children('a').css('background','red').parent().sibling().children('a').css('background', 'white');
    }

})