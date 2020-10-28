package br.com.ejs.projeto.integrador

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.activity_tela_inicial.*
import kotlinx.android.synthetic.main.login.*
import kotlinx.android.synthetic.main.nav_view.*
import kotlinx.android.synthetic.main.toolbar.*

 class TelaInicialActivity : DebugActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_inicial)


        this.drawerLayout = layoutMenuLateral
        this.navView = menu_lateral



        setSupportActionBar(toolbar_view)

        supportActionBar?.title = "Tela Inicial"
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        configuraMenuLateral()
    }




    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val id = item?.itemId

        if (id == R.id.action_atualizar) {
            Toast.makeText(this, "Botao atualizar", Toast.LENGTH_LONG).show()

        } else if (id == R.id.action_buscar) {
            Toast.makeText(this, "Botao buscar", Toast.LENGTH_LONG).show()

        }else if (id == R.id.action_config){
            Toast.makeText(this, "Botao configurar", Toast.LENGTH_LONG).show()
        } else if(id == android.R.id.home){
            finish()
        }

    return super.onOptionsItemSelected(item)
     }

}