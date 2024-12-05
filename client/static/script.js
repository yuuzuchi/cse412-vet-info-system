document.querySelectorAll('.menu li').forEach((item) => {
    item.addEventListener('click', () => {
      
      document.querySelector('.menu .active').classList.remove('active');
      
      item.classList.add('active');
      
      const topBarTitle = document.querySelector('.top-bar h1');
      topBarTitle.textContent = `Welcome to ${item.textContent}`;
    });
  });
  