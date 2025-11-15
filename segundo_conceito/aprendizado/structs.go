package apd2

import (
	"fmt"
)

func AprendendoStruct(){

type pessoa struct{
	nome string
	idade int
}

	pessoas := []pessoa{
		{"Paulo", 32},
		{"Henrique", 79},
	}

	for indice, pessoa := range pessoas{
		fmt.Printf("%d° Pessoa chamada: %s tem %d anos\n",(indice + 1) ,pessoa.nome, pessoa.idade)
	}

}