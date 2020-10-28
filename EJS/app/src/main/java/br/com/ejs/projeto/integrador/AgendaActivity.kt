package br.com.ejs.projeto.integrador

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_agenda.*
import kotlinx.android.synthetic.main.activity_check_in_out.*
import kotlinx.android.synthetic.main.activity_check_in_out.layoutMenuLateral

import kotlinx.android.synthetic.main.nav_view.*
import kotlinx.android.synthetic.main.toolbar.*

class AgendaActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_agenda)

        this.drawerLayout = layoutMenuLateral
        this.navView = menu_lateral

        setSupportActionBar(toolbar_view)

        supportActionBar?.title = "Agenda"
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        configuraMenuLateral()
    }
}