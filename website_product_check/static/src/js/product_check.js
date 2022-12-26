/** @odoo-module **/

$(document).ready(function() {

    $("#available").hide();
    $("#not_available").hide();
    $("#product_check").on('change',function(){
        console.log("qwertyu")
        var quan = $("#product_check").val();
//        console.log(quan)
        var quantity = parseFloat(quan)
        var num = Number.isNaN(quantity)
        console.log(quantity, "ooooooooooooooo")
        console.log(num, "vggggggggggggggggg")
        if(!num){
        $("#available").show();
        $("#not_available").hide();
        console.log("available")
        }
        if (num || quantity <=0){
        $("#not_available").show();
        $("#available").hide();
        console.log("not_available")
        }
        document.getElementById("qty_available").innerHTML = quan;
    })
})