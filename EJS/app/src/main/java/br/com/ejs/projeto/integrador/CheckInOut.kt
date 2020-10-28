package br.com.ejs.projeto.integrador

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_check_in_out.*

import kotlinx.android.synthetic.main.nav_view.*
import kotlinx.android.synthetic.main.toolbar.*

class CheckInOut : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_check_in_out)

        this.drawerLayout = layoutMenuLateral
        this.navView = menu_lateral

        setSupportActionBar(toolbar_view)

        supportActionBar?.title = "Check in/ out"
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        configuraMenuLateral()
    }
}