$(document).ready(function () {
  var form = $('#form_buying_product');
  console.log(form);

  function basketUpdating(product_id, nmb, is_delete){
    var data = {};
    data.product_id = product_id;
    data.nmb = nmb;
    var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;


    if (is_delete){
      data["is_delete"] = true;
    }


    var url = form.attr("action");

    console.log(data)
    $.ajax({
      url: url,
      type: 'POST',
      data: data,
      cache: true,
      success: function (data){
        console.log("OK");
        console.log(data.products_total_nmb);
        if (data.products_total_nmb || data.products_total_nmb == 0 ) {
          $('#basket_total_nmb').text("(" + data.products_total_nmb + ")" );
          console.log(data.products);
          $('.basket-items ul').html("");
          $.each(data.products, function (k, v) {
            $('.basket-items ul').append('<li>'+ v.name+ ', '+ v.nmb+ 'шт. '+ 'по '+ v.price_per_item + ' грн.   ' +
              '<a class="glyphicon glyphicon-remove delete-item" aria-hidden="true" href="" data-product_id="'+v.id +'"></a>' +
            '</li>');
          });
        }
      },
      error: function (){
        console.log('error');
      }
    })
  };



  form.on('submit',function (e) {
    e.preventDefault();
    var form = $(this);
    var nmb = $('#number').val();
    //console.log(nmb);
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data("product_id");
    var name = submit_btn.data("name");
    //console.log(product_id);
    //console.log(name);
    var price = submit_btn.data("price");
    //console.log(price);


    basketUpdating(product_id, nmb, is_delete=false)

  });



  $(document).on('click', '.delete-item', function (e) {
    e.preventDefault();
    product_id = $(this).data("product_id");
    nmb = 0;
    basketUpdating(product_id, nmb, is_delete=true)

  });

  function calculatingBasketAmount(){
    var total_order_amount = 0;
    $('.total-product-in-basket-amount').each(function(){
      total_order_amount = total_order_amount + parseFloat($(this).text());
    });
    console.log(total_order_amount);
    $('#total_order_amount').text(total_order_amount);
  };

  $(document).on('change', '.product-in-basket-nmb', function () {
    var current_nmb = $(this).val();
    console.log(current_nmb);
    var current_tr = $(this).closest('tr');
    //var lol = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
    //console.log(lol);
    var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
    console.log(current_price);
    var total_amount = parseFloat(current_nmb * current_price).toFixed(2);
    console.log(total_amount);
    current_tr.find('.total-product-in-basket-amount').text(total_amount);
    calculatingBasketAmount();

  });
  calculatingBasketAmount();

});
