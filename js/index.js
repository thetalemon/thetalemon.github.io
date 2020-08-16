var animation = bodymovin.loadAnimation({
  container: document.getElementById('star'),
  renderer: 'svg',
  loop: false,
  autoplay: false,
  path: 'data.json'
});

const element = document.getElementById('star');

element.addEventListener('click', function(){
  if(element.classList.contains('clicked')){
    animation.playSegments([0,5], true);
    element.classList.remove('clicked');
  }else{
    animation.playSegments([0,120], true);
    element.classList.add('clicked');
  }
 });

// This is a soruce for Jquery
//
// starIcon = $('#star');
//
// starIcon.on('click', function(){
//   if(!starIcon.hasClass('clicked')) {
//     animation.playSegments([0,30], true);
//     starIcon.addClass('clicked');
//     } else {
//       animation.playSegments([0,1], true);
//       starIcon.removeClass('clicked');
//     }
// });