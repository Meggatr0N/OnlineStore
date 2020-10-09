$(document).ready(function () {
  var form = $('#form_buying_product');
  console.log(form);

  function basketUpdating(product_id, nmb, is_delete){
    var data = {};
    data.product_id = product_id;


    console.log("product_id is " + nmb);
    console.log(nmb);


    if (nmb){
      data.nmb = nmb;
    } else {
      data.nmb = 1;
    }

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



  //form.on('submit',function (e) {
  //  e.preventDefault();
  //  var form = $(this);
  //  var nmb = $('#number').val();
  //  //console.log(nmb);
  //  var submit_btn = $('#submit_btn');
  //  var product_id = submit_btn.data("product_id");
  //  var name = submit_btn.data("name");
  //  //console.log(product_id);
  //  //console.log(name);
  //  var price = submit_btn.data("price");
  //  //console.log(price);
//
//
  //  basketUpdating(product_id, nmb, is_delete=false)
//
  //});

  form.on('submit',function(e){
    e.preventDefault();
    var form = $(this);
    var nmb = $('#number').val();
    var submit_btn = form.find($('#submit_btn'));
    var product_id = submit_btn.data("product_id");
    var product_name = submit_btn.data("name")
    var product_price = submit_btn.data("price")

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






// Логика работы слайдера
//https://itchief.ru/javascript/how-to-create-slider
'use strict';
var slideShow = (function () {
  return function (selector, config) {
    var
      _slider = document.querySelector(selector), // основный элемент блока
      _sliderContainer = _slider.querySelector('.slider__items'), // контейнер для .slider-item
      _sliderItems = _slider.querySelectorAll('.slider__item'), // коллекция .slider-item
      _sliderControls = _slider.querySelectorAll('.slider__control'), // элементы управления
      _currentPosition = 0, // позиция левого активного элемента
      _transformValue = 0, // значение трансформации .slider_wrapper
      _transformStep = 100, // величина шага (для трансформации)
      _itemsArray = [], // массив элементов
      _timerId,
      _indicatorItems,
      _indicatorIndex = 0,
      _indicatorIndexMax = _sliderItems.length - 1,
      _stepTouch = 50,
      _config = {
        isAutoplay: false, // автоматическая смена слайдов
        directionAutoplay: 'next', // направление смены слайдов
        delayAutoplay: 5000, // интервал между автоматической сменой слайдов
        isPauseOnHover: true // устанавливать ли паузу при поднесении курсора к слайдеру
      };

    // настройка конфигурации слайдера в зависимости от полученных ключей
    for (var key in config) {
      if (key in _config) {
        _config[key] = config[key];
      }
    }

    // наполнение массива _itemsArray
    for (var i = 0, length = _sliderItems.length; i < length; i++) {
      _itemsArray.push({ item: _sliderItems[i], position: i, transform: 0 });
    }

    // переменная position содержит методы с помощью которой можно получить минимальный и максимальный индекс элемента, а также соответствующему этому индексу позицию
    var position = {
      getItemIndex: function (mode) {
        var index = 0;
        for (var i = 0, length = _itemsArray.length; i < length; i++) {
          if ((_itemsArray[i].position < _itemsArray[index].position && mode === 'min') || (_itemsArray[i].position > _itemsArray[index].position && mode === 'max')) {
            index = i;
          }
        }
        return index;
      },
      getItemPosition: function (mode) {
        return _itemsArray[position.getItemIndex(mode)].position;
      }
    };

    // функция, выполняющая смену слайда в указанном направлении
    var _move = function (direction) {
      var nextItem, currentIndicator = _indicatorIndex;;
      if (direction === 'next') {
        _currentPosition++;
        if (_currentPosition > position.getItemPosition('max')) {
          nextItem = position.getItemIndex('min');
          _itemsArray[nextItem].position = position.getItemPosition('max') + 1;
          _itemsArray[nextItem].transform += _itemsArray.length * 100;
          _itemsArray[nextItem].item.style.transform = 'translateX(' + _itemsArray[nextItem].transform + '%)';
        }
        _transformValue -= _transformStep;
        _indicatorIndex = _indicatorIndex + 1;
        if (_indicatorIndex > _indicatorIndexMax) {
          _indicatorIndex = 0;
        }
      } else {
        _currentPosition--;
        if (_currentPosition < position.getItemPosition('min')) {
          nextItem = position.getItemIndex('max');
          _itemsArray[nextItem].position = position.getItemPosition('min') - 1;
          _itemsArray[nextItem].transform -= _itemsArray.length * 100;
          _itemsArray[nextItem].item.style.transform = 'translateX(' + _itemsArray[nextItem].transform + '%)';
        }
        _transformValue += _transformStep;
        _indicatorIndex = _indicatorIndex - 1;
        if (_indicatorIndex < 0) {
          _indicatorIndex = _indicatorIndexMax;
        }
      }
      _sliderContainer.style.transform = 'translateX(' + _transformValue + '%)';
      _indicatorItems[currentIndicator].classList.remove('active');
      _indicatorItems[_indicatorIndex].classList.add('active');
    };

    // функция, осуществляющая переход к слайду по его порядковому номеру
    var _moveTo = function (index) {
      var i = 0, direction = (index > _indicatorIndex) ? 'next' : 'prev';
      while (index !== _indicatorIndex && i <= _indicatorIndexMax) {
        _move(direction);
        i++;
      }
    };

    // функция для запуска автоматической смены слайдов через промежутки времени
    var _startAutoplay = function () {
      if (!_config.isAutoplay) {
        return;
      }
      _stopAutoplay();
      _timerId = setInterval(function () {
        _move(_config.directionAutoplay);
      }, _config.delayAutoplay);
    };

    // функция, отключающая автоматическую смену слайдов
    var _stopAutoplay = function () {
      clearInterval(_timerId);
    };

    // функция, добавляющая индикаторы к слайдеру
    var _addIndicators = function () {
      var indicatorsContainer = document.createElement('ol');
      indicatorsContainer.classList.add('slider__indicators');
      for (var i = 0, length = _sliderItems.length; i < length; i++) {
        var sliderIndicatorsItem = document.createElement('li');
        if (i === 0) {
          sliderIndicatorsItem.classList.add('active');
        }
        sliderIndicatorsItem.setAttribute("data-slide-to", i);
        indicatorsContainer.appendChild(sliderIndicatorsItem);
      }
      _slider.appendChild(indicatorsContainer);
      _indicatorItems = _slider.querySelectorAll('.slider__indicators > li')
    };

    var _isTouchDevice = function () {
      return !!('ontouchstart' in window || navigator.maxTouchPoints);
    };

    // функция, осуществляющая установку обработчиков для событий
    var _setUpListeners = function () {
      var _startX = 0;
      if (_isTouchDevice()) {
        _slider.addEventListener('touchstart', function (e) {
          _startX = e.changedTouches[0].clientX;
          _startAutoplay();
        });
        _slider.addEventListener('touchend', function (e) {
          var
            _endX = e.changedTouches[0].clientX,
            _deltaX = _endX - _startX;
          if (_deltaX > _stepTouch) {
            _move('prev');
          } else if (_deltaX < -_stepTouch) {
            _move('next');
          }
          _startAutoplay();
        });
      } else {
        for (var i = 0, length = _sliderControls.length; i < length; i++) {
          _sliderControls[i].classList.add('slider__control_show');
        }
      }
      _slider.addEventListener('click', function (e) {
        if (e.target.classList.contains('slider__control')) {
          e.preventDefault();
          _move(e.target.classList.contains('slider__control_next') ? 'next' : 'prev');
          _startAutoplay();
        } else if (e.target.getAttribute('data-slide-to')) {
          e.preventDefault();
          _moveTo(parseInt(e.target.getAttribute('data-slide-to')));
          _startAutoplay();
        }
      });
      document.addEventListener('visibilitychange', function () {
        if (document.visibilityState === "hidden") {
          _stopAutoplay();
        } else {
          _startAutoplay();
        }
      }, false);
      if (_config.isPauseOnHover && _config.isAutoplay) {
        _slider.addEventListener('mouseenter', function () {
          _stopAutoplay();
        });
        _slider.addEventListener('mouseleave', function () {
          _startAutoplay();
        });
      }
    };

    // добавляем индикаторы к слайдеру
    _addIndicators();
    // устанавливаем обработчики для событий
    _setUpListeners();
    // запускаем автоматическую смену слайдов, если установлен соответствующий ключ
    _startAutoplay();

    return {
      // метод слайдера для перехода к следующему слайду
      next: function () {
        _move('next');
      },
      // метод слайдера для перехода к предыдущему слайду
      left: function () {
        _move('prev');
      },
      // метод отключающий автоматическую смену слайдов
      stop: function () {
        _config.isAutoplay = false;
        _stopAutoplay();
      },
      // метод запускающий автоматическую смену слайдов
      cycle: function () {
        _config.isAutoplay = true;
        _startAutoplay();
      }
    }
  }
}());

slideShow('.slider', {
  isAutoplay: false
});
