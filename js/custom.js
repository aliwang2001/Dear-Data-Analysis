

//Author: Alicia Wang
//Date: June 18th 2018
/*-----------------------------------------------*/


// PACKERY JAVASCRIPT FUNCTION
$(function () {
  var $container = $('#packery-container');
  $container.packery({
    itemSelector: '.col-md-3',
    layoutMode: 'fitRows',
    columnWidth: $container.find('.col-md-3')[0],
  });

  // get item elements, jQuery-ify them
  var $itemElems = $($container.packery('getItemElements'));
  // make item elements draggable
  $itemElems.each(function (i, itemElem) {
    // make element draggable with Draggabilly
    var draggie = new Draggabilly(itemElem);
    // bind Draggabilly events to Packery
    $container.packery('bindDraggabillyEvents', draggie);
  });
  // bind Draggable events to Packery
  $container.packery('bindUIDraggableEvents', $itemElems);
  // stamp item after dragging
  $container.packery('on', 'dragItemPositioned', function (pckryInstance, draggedItem) {
    setTimeout(function () {
      $container.packery();
    }, 50);
  });
});


/* jQuery Pre loader
 -----------------------------------------------*/
/*
$('#loadpls').load(function(){
  $('.preloader').fadeOut(1000); // set duration in brackets    
});
*/

var $container;
var filters = {};

$(function () {
  $container = $('#container');

  createContent();

  var $grid = $('#container').isotope({
    itemSelector: '.item',
  });
  var iso = $grid.data('isotope');

  /*
  var $giorgiapercentgrid = $('#container').isotope({
    itemSelector: '.Giorgia',
  });
  var giorgiapercent = $giorgiapercentgrid.data('isotope');

  var $stefaniepercentgrid = $('#container').isotope({
    itemSelector: '.Stefanie',
  });
  var stefaniepercent = $stefaniepercentgrid.data('isotope');
*/
  var $filterDisplay = $('#filter-display');
  var $filterCount = $('#filter-count');
  var $filterButtons = $('.filters .checkbox');

  //var $spercentages = $('#spercentages');
  // var $gpercentages = $('#gpercentages');


  $container.isotope();
  // do stuff when checkbox change
  $('#options').on('change', function (jQEvent) {
    var $checkbox = $(jQEvent.target);
    manageCheckbox($checkbox);

    var comboFilter = getComboFilter(filters);

    $container.isotope({ filter: comboFilter });

    $filterCount.text(iso.filteredItems.length + ' items');

    $filterDisplay.text(comboFilter);

    updateFilterCounts();

    //$spercentages.text( 'Used by Stefanie ' + stefaniepercent.filteredItems.length/52*100 + '% of the time'  );
    //$gpercentages.text( 'Used by Giorgia ' + giorgiapercent.filteredItems.length/52*100 + '% of the time'  );

  });

});


/*
var data = {
  brands: 'brand1 brand2 brand3 brand4'.split(' '),
  productTypes: 'type1 type2 type3 type4'.split(' '),
  colors: 'red blue yellow green'.split(' '),
  sizes: 'uk-size8 uk-size9 uk-size10 uk-size11'.split(' ')
};
*/
function createContent() {
  var items = '';
  $container.append(items);
}


function getComboFilter(filters) {
  var i = 0;
  var comboFilters = [];
  var message = [];

  for (var prop in filters) {
    message.push(filters[prop].join(' '));
    var filterGroup = filters[prop];
    // skip to next filter group if it doesn't have any values
    if (!filterGroup.length) {
      continue;
    }
    if (i === 0) {
      // copy to new array
      comboFilters = filterGroup.slice(0);
    } else {
      var filterSelectors = [];
      // copy to fresh array
      var groupCombo = comboFilters.slice(0); // [ A, B ]
      // merge filter Groups
      for (var k = 0, len3 = filterGroup.length; k < len3; k++) {
        for (var j = 0, len2 = groupCombo.length; j < len2; j++) {
          filterSelectors.push(groupCombo[j] + filterGroup[k]); // [ 1, 2 ]
        }

      }
      // apply filter selectors to combo filters for next group
      comboFilters = filterSelectors;
    }
    i++;
  }

  var comboFilter = comboFilters.join(', ');
  return comboFilter;
}

function manageCheckbox($checkbox) {
  var checkbox = $checkbox[0];

  var group = $checkbox.parents('.option-set').attr('data-group');
  // create array for filter group, if not there yet
  var filterGroup = filters[group];
  if (!filterGroup) {
    filterGroup = filters[group] = [];
  }

  var isAll = $checkbox.hasClass('all');
  // reset filter group if the all box was checked
  if (isAll) {
    delete filters[group];
    if (!checkbox.checked) {
      checkbox.checked = 'checked';
    }
  }
  // index of
  var index = $.inArray(checkbox.value, filterGroup);

  if (checkbox.checked) {
    var selector = isAll ? 'input' : 'input.all';
    $checkbox.siblings(selector).removeAttr('checked');


    if (!isAll && index === -1) {
      // add filter to group
      filters[group].push(checkbox.value);
    }

  } else if (!isAll) {
    // remove filter from group
    filters[group].splice(index, 1);
    // if unchecked the last box, check the all
    if (!$checkbox.siblings('[checked]').length) {
      $checkbox.siblings('input.all').attr('checked', 'checked');
    }
  }

}

/*
function updateFilterCounts()  {
  // get filtered item elements
  var itemElems = $grid.isotope('getFilteredItemElements');
  var $itemElems = $( itemElems );
  $filterButtons.each( function( i, button ) {
    var $button = $( button );
    var filterValue = $button.attr('data-filter');
    if ( !filterValue ) {
      // do not update 'any' buttons
      return;
    }
    var count = $itemElems.filter( filterValue ).length;
    $button.find('.filter-count').text( '(' + count +')' );
  });
}
*/



/* Isotope Filter --VERSION OLD--
-----------------------------------------------
jQuery(document).ready(function($){

  if ( $('.iso-box-wrapper').length > 0 ) { 

      var $container  = $('.iso-box-wrapper'), 
        $imgs     = $('.iso-box img');

      $container.imagesLoaded(function () {

        $container.isotope({
        layoutMode: 'fitRows',
        itemSelector: '.iso-box'
        });

        $imgs.load(function(){
          $container.isotope('reLayout');
        })

      });

      //filter items on button click

      $('.filter-wrapper li a').click(function(){

          var $this = $(this), filterValue = $this.attr('data-filter');

      $container.isotope({ 
        filter: filterValue,
        animationOptions: { 
            duration: 750, 
            easing: 'linear', 
            queue: false, 
        }                
      });             

      // don't proceed if already selected 

      if ( $this.hasClass('selected') ) { 
        return false; 
      }

      var filter_wrapper = $this.closest('.filter-wrapper');
      filter_wrapper.find('.selected').removeClass('selected');
      $this.addClass('selected');

        return false;
      }); 

  }

});
*/

/* Navigation Bar
 -----------------------------------------------*/
/*
$(document).ready(function() { 
    "use strict";

    // Navbar Sticky

    (function() {
        var docElem = document.documentElement,
            didScroll = false,
            stickynav = 50;
            document.querySelector( '.nav-container' );
        function init() {
            window.addEventListener( 'scroll', function() {
                if( !didScroll ) {
                    didScroll = true;
                    setTimeout( scrollPage, 50 );
                }
            }, false );
        }
        
        function scrollPage() {
            var sy = scrollY();
            if ( sy >= stickynav ) {
                $( '.nav-container' ).addClass('sticky');
            }
            else {
                $( '.nav-container' ).removeClass('sticky');
            }
            didScroll = false;
        }
        
        function scrollY() {
            return window.pageYOffset || docElem.scrollTop;
        }        
        init();        
    })();

});
*/

$(document).ready(function () {

  "use strict";

  $('.menu-container').each(function (index) {
    $(this).find('.circle').attr('menu-link', index);
    $(this).find('.list-menu').clone().appendTo('body').attr('menu-link', index);
  });

  $('.menu-container .circle').click(function () {
    var linkedVideo = $('section').closest('body').find('.list-menu[menu-link="' + $(this).attr('menu-link') + '"]');
    linkedVideo.toggleClass('reveal-modal');

  });

  $('section').closest('body').find('.close-iframe').click(function () {
    $(this).closest('.list-menu').toggleClass('reveal-modal');
  });


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

});


  /* MODAL SERVICE --VERSION OLD--
  -------------------------------*/
  /*
  const modalService = () => {
    const d = document;
    const body = d.querySelector('body');
    const buttons = d.querySelectorAll('[data-modal-trigger]');
    
    // attach click event to all modal triggers
    for(let button of buttons) {
      triggerEvent(button);
    }
    
    function triggerEvent(button) {
      button.addEventListener('click', () => {
        const trigger = button.getAttribute('data-modal-trigger');
        const modal = d.querySelector(`[data-modal=${trigger}]`);
        const modalBody = modal.querySelector('.modal-body');
        const closeBtn = modal.querySelector('.close');
        
        closeBtn.addEventListener('click', () => modal.classList.remove('is-open'))
        modal.addEventListener('click', () => modal.classList.remove('is-open'))
        
        modalBody.addEventListener('click', (e) => e.stopPropagation());
  
        modal.classList.toggle('is-open');
        
        // Close modal when hitting escape
        body.addEventListener('keydown', (e) => {
          if(e.keyCode === 27) {
            modal.classList.remove('is-open')
          }
        });
      });
    }
  }
  modalService();
  */