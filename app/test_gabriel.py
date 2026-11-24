from app import app 
 
<<<<<<< HEAD
def test_saude_tem_versao():     
  dados = app.test_client().get("/saude").get_json()
  assert "versao" in dados 

def test_rota_inexistente_da_404():     
  assert app.test_client().get("/nao-existe").status_code == 404 
=======
 
def test_saude_tem_versao():
      dados = app.test_client().get("/saude").get_json()
      assert "versao" in dados 
      
def test_rota_inexistente_da_404():    
      assert app.test_client().get("/nao-existe").status_code == 404 
>>>>>>> refs/remotes/origin/main
