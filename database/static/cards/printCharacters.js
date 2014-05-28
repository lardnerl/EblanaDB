/*
var characters = [];

$(
	function()
	{
		var get = getQueryVariables();
		var urlVars = get;
		var idEvent = urlVars['idEvent'];
		$.post(
			'godStaff.php',
			{
				'act':'fetchCharactersForEvent',
				'idEvent':idEvent
			},
			loadCharacters
		);
	}
);

function loadCharacters(xmlResponse)
{
	var characterNodes = $(xmlResponse.documentElement).find('perksets');
	
	characterNodes.each(
		function()
		{
			var xml = $(this);
			var characterNode = xml.children('character').first();
			var c = new Character(characterNode.attr('idcharacters'), characterNode.attr('name'), characterNode.attr('race'));
			c.buildFromXML(xml);
			c.showPrintFormat($('#charactersForPrinting'));
		}
	);
}

function getQueryVariables()
{ 
	var query = window.location.search.substring(1); 
	var vars = query.split("&");
	var pairs = {};
	for (var i=0;i<vars.length;i++)
	{ 
		var pair = vars[i].split("=");
		pairs[pair[0]] = pair[1];
	}
	return pairs;
}
*/