$('#show_confirmation').click(function() {
    Swal.fire({
      title: '¿Está seguro?',
      text: "No podrá revertir la acción",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'Cancelar.',
      confirmButtonText: 'Si,crear.'
    }).then((result) => {
      if (result.isConfirmed) {       
        $(
          '#send'
        ).submit();
      }
    })


  })