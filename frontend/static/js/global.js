
  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

 const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }
  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  function loaderBtn(condition, id) {
        if (condition === true) {
            $(id).addClass('loading disabled');
            $(id).prop('disabled', true);
            $(id).data("temp-name", $(id).text());
            $(id).html('processing...');
        } else {
            $(id).html($(id).data("temp-name"));
            $(id).removeClass('loading disabled');
            $(id).prop('disabled', false);
        }
    }