package apd3

import (
	"fmt"
	"encoding/json"
)

func InfoInteroperabilidade()  {


	type Pessoa struct{
		Nome string `json:"nome"`
		Idade int `json:"idade"`
		Cpf string `json:"cpf"`
	} 

	p := Pessoa{"Paulo", 32, "123.456.789-00"}
	data, _ := json.Marshal(p)
	fmt.Print(string(data))
}