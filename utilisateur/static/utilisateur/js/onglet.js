var tabs = document.querySelectorAll('.tabs a');
	// Fonction de traitement des onglets ************************
var afficherOnglet = function(a, animations){
		// Les variables
		var li = a.parentNode,
			parent = a.parentNode.parentNode.parentNode, // on se positionne sur le parent div (a->li->ul->div)
			id = a.getAttribute('href'),
			tabActif = parent.querySelector('.tab-content.active'),
			tabaAfficher = parent.querySelector(id);

			if(animations === undefined){
				animations = true;
			}

		// On vérifie si le parent de l'élément (li) pocède la classe active
		if(li.classList.contains('active')){
			return false; // on ne fais rien
		}

		// On retire la classe active à l'élément déjà active (li)
		parent.querySelector('.tabs .active').classList.remove('active'); // on retire la classe active à l'élément qui le pocédait

		// On ajoute la class active sur le li en cours
		li.classList.add('active');

		// on assigne la fonction des transition à une variable pour pouvoir la supprimer
		var finDeTransition = function(){
			this.classList.remove('fade'); // On retire la class fade à l'élément actif
			this.classList.remove('active'); // On lui retire la class active

			// On ajoute les class suivantes à l'élément(div) à afficher
			tabaAfficher.classList.add('active');
			tabaAfficher.classList.add('fade');
			tabaAfficher.offsetWidth;
			tabaAfficher.classList.add('in');

			// On supprime l'évènement
			tabActif.removeEventListener('transitionend',finDeTransition,false);
		};

		if(animations){ // On active la transition
			// On ajoute la class fade à l'élément actif pour le masquer (opacity = 0)
			tabActif.classList.add('fade');
			// On retire la class in au cas ou il la pocède
			tabActif.classList.remove('in');

			// On ajoute un évènement de fin de transition sur la tab actif
			tabActif.addEventListener('transitionend',finDeTransition,false);
		} else { // On n'a pas de transition
			// On retire la classe active à l'élément déjà active (div)
			tabActif.classList.remove('active');

			// On ajoute la class active sur le div correspondant à l'élément en cours
			tabaAfficher.classList.add('active');
		}



	};
	// Fin de la fonction afficheOnglet **********************

// On parcours les liens sélectionnés
for (var i = 0, c = tabs.length; i < c; i++) {
	// On ajoute un évènement d'écoute sur chaque élément
	tabs[i].addEventListener('click',function(e){
		afficherOnglet(this, true);
	},false);
}

// On récupère le hash de la page (l'ancre dans le navigateur)
	var hashChange = function(e){
		var hash = window.location.hash,
		a = document.querySelector('a[href="'+ hash +'"]');
		if(a !== null && !a.classList.contains('active')){
			afficherOnglet(a, e !== undefined);
		}
	};


// On ajoute un évènement d'écoute à windows pour vérifier lorsque le hashchange
window.addEventListener('hashchange',hashChange,false);
hashChange();