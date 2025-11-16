package std4

import (
    "database/sql"
    "log"

    _ "modernc.org/sqlite"
)

var DB *sql.DB

func Conect(){
	var err error

	DB, err = sql.Open("sqlite", "./meubanco.db")
	if err != nil{
		log.Fatal(err)
	}

	createtable := `
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            cpf TEXT
        );
    `

	_, err = DB.Exec(createtable)

	if err != nil{
		log.Fatal(err)
	}
	log.Print("sucesso")
}

func InserirUsuario(nome string, idade int, cpf string) error {
    query := `INSERT INTO usuarios (nome, idade, cpf) VALUES (?, ?, ?)`
    _, err := DB.Exec(query, nome, idade, cpf)
    return err
}

type Usuario struct{
	Id int
	Nome string
	Idade int
	Cpf string
}

func ListarUsuarios() ([]Usuario, error){
	rows, err := DB.Query("SELECT id, nome, idade, cpf FROM usuarios")
	if err != nil{
		return nil, err
	}
	defer rows.Close()

	var lista []Usuario

	for rows.Next(){
		var u Usuario
		rows.Scan(&u.Id,&u.Nome,&u.Idade,&u.Cpf)
		lista = append(lista, u)
	}
	return lista, nil
}

func BuscarPorId(id int) (Usuario, error){
	var u Usuario
	err := DB.QueryRow("SELECT id, nome, idade, cpf FROM usuarios WHERE id = ?", id).
	Scan(&u.Id, &u.Nome, &u.Idade, &u.Cpf)
	return u, err
}

func AtualizarUsuario(id int, nome string, idade int, cpf string) error {
	query := `UPDATE usuarios SET nome =?, idade =?, cpf =? WHERE id =?`
	_, err := DB.Exec(query, nome, idade, id, cpf)
	return err
}
func DeletarUsuario(id int) error {
	query := `DELETE FROM usuarios WHERE id = ?`
	_, err := DB.Exec(query, id)
	return err
}