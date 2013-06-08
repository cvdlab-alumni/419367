function export(lar_model){
	var V = lar_model[0];
	var FV = lar_model[1];
	var output +="# List of Vertices"+"\n";
	for (var i = 0; i < V.length; i++){
			output += "v "+V[i][0]+" "+V[i][1]+" "+V[i][2]+" "+V[i][3]+"\n";
	}
	output += "# Face Definitions"+"\n";
	output += "f " +FV[0][0]+FV[0][1]+FV[0][2];
	for (var j=1; j<FV.length;j++){
		output+= FV[j][0]+"/"+FV[j][1]+"/"+FV[j][2]+"\n";
	}
return output;
}