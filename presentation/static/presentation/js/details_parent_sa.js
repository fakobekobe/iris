$(document).ready(function(){

// ******************* GESTION DE L'AJOUT D'UN ETAT DE SANTE *****************************

    var envoyer_etatsante = $('#envoyer_etatsante');
    var select_typeetatsante = $('#select_typeetatsante');
    var dateenre_e = $('#dateenre_e');
    var form_etatsante = $('#form_etatsante');
    var tableetatsante = $('#tableetatsante tbody');
    var valider_e = true;


    // Traitement AJAX
    envoyer_etatsante.click(function(e){
        e.preventDefault(); // On annule l'envoi du formulaire
        if(!select_typeetatsante.val()){
            valider_e = false;
            alert("Veuillez sélectionner le type d'état de santé.");
            select_typeetatsante.focus();
        }else if(!dateenre_e.val()){
            valider_e = false;
            alert("Veuillez renseigner la date d'enregistrement.");
            dateenre_e.focus();
        }else{
            valider_e = true;
        }

        if(valider_e){
                // On instancie un objet formulaire pour l'envoi des champs du formulaire
                var formData = new FormData(form_etatsante[0]);

                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/presentation/ajouter-etatsante-parent", // On ajoute l'url absolue en commençant par la racine
                    type: 'POST',
                    data: formData,
                    success: function(data){

                        // On vide le contenu
                        tableetatsante.html('');

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tableetatsante.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typeetatsante + `</td>
                                    <td>` + valeur.dateenre + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#etatsantesupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="etatsantesupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Etat de santé : <strong>` + valeur.typeetatsante + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <input type="text" name="id_parent_etatsante_s" id="id_parent_etatsante_s` + valeur.id + `" value="` + valeur.id_parent + `" hidden>
                                                            <button type="submit" name="supprimer_e" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_e" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);
                        });

                        // Affichage du toast ---------
                        var btn = $('#btn_ferme_toast_success');
                        var toast = $('#mytoast_success');
                            toast.addClass('show');
                            btn.click(function(){
                                toast.removeClass('show');
                            });
                         var montemps = setInterval(function(){
                            toast.removeClass('show');
                            clearInterval(montemps);
                         }, 3000);
                         // Fin toast -----------

                        supprimer_ligne_etatsante(); // On appelle la fonction pour prendre en compte les nouvelles données
                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez réessayer car une erreur est survenue.');
                             },
                    },
                    cache: false,
                    contentType: false,
                    processData: false,
                });

        }

    });


// ******************* GESTION DE LA SUPPRESSION D'UN ETAT DE SANTE *****************************
    function supprimer_ligne_etatsante(){
        var supprimer_e = $('button[name=supprimer_e]');
        var annuler_e = $('button[name=annuler_e]');

        // Traitement AJAX
        supprimer_e.each(function(){
            $(this).click(function(e){
                e.preventDefault();

                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/presentation/supprimer-etatsante-parent", // On ajoute l'url absolue en commençant par la racine
                    type: 'get',
                    data: {
                        id_parent_etatsante_s: $('#id_parent_etatsante_s'+$(this).val()).val(),
                        supprimer_e: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tableetatsante.html('');

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tableetatsante.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typeetatsante + `</td>
                                    <td>` + valeur.dateenre + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#etatsantesupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="etatsantesupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Etat de santé : <strong>` + valeur.typeetatsante + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <input type="text" name="id_parent_etatsante_s" id="id_parent_etatsante_s` + valeur.id + `" value="` + valeur.id_membre + `" hidden>
                                                            <button type="submit" name="supprimer_e" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_e" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);

                        });

                        annuler_e.trigger('click');

                        // Affichage du toast ---------
                        var btn = $('#btn_ferme_toast_suppression');
                        var toast = $('#mytoast_suppression');
                            toast.addClass('show');
                            btn.click(function(){
                                toast.removeClass('show');
                            });
                         var montemps = setInterval(function(){
                            toast.removeClass('show');
                            clearInterval(montemps);
                         }, 3000);
                         // Fin toast -----------

                        supprimer_ligne_etatsante();
                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez réessayer car une erreur est survenue.');
                             },
                    },
                });

            });
        });
    }

    supprimer_ligne_etatsante(); // On appelle la fonction


// ****************************************************************************

});