$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=parseFloat(data.amount).toFixed(2);
            document.getElementById("totalamount").innerText=parseFloat(data.totalamount).toFixed(2);
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=parseFloat(data.amount).toFixed(2);
            document.getElementById("totalamount").innerText=parseFloat(data.totalamount).toFixed(2);
        }
    })
})

$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerText=parseFloat(data.amount).toFixed(2);
            document.getElementById("totalamount").innerText=parseFloat(data.totalamount).toFixed(2);
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})
