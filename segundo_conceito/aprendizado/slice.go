package apd2

import (
	"fmt"
)

func SliceSimples(){

nomes := []string{"Ana", "Bia", "Carlos", "Daniel"}

for indice, valor := range nomes{
	fmt.Println((indice + 1),valor)
}

}
