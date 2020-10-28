
import os
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app_settings = os.getenv(
    'APP_SETTINGS',
    'tmsApp.config_files.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

if __name__ == "__main__":
    import tmsApp.controllers.authCtrl as auth
    import tmsApp.controllers.usuarioCtrl as usuario
    import tmsApp.controllers.colaboradorCtrl as colaborador
    import tmsApp.controllers.clienteCtrl as cliente
    import tmsApp.controllers.fornecedorCtrl as fornecedor
    import tmsApp.controllers.veiculoCtrl as veiculo
    import tmsApp.controllers.demDiarioCtrl as demDiario
    import tmsApp.controllers.manutencaoCtrl as manutencao
    import tmsApp.controllers.rdvoCtrl as rdvo
    import tmsApp.controllers.multaCtrl as multa
    import tmsApp.controllers.fuelCardCtrl as fuelCard
    import tmsApp.controllers.combustivelCtrl as combustivel
    import tmsApp.controllers.cargoCtrl as cargo
    import tmsApp.controllers.departamentoCtrl as departamento
    import tmsApp.controllers.grupoCtrl as grupo
    import tmsApp.controllers.controlColabCtrl as controlColab

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(usuario.usuario_bp)
    app.register_blueprint(colaborador.colaborador_bp)
    app.register_blueprint(cliente.cliente_bp)
    app.register_blueprint(fornecedor.fornecedor_bp)
    app.register_blueprint(veiculo.veiculo_bp)
    app.register_blueprint(demDiario.demDiario_bp)
    app.register_blueprint(manutencao.manutencao_bp)
    app.register_blueprint(rdvo.rdvo_bp)
    app.register_blueprint(multa.multa_bp)
    app.register_blueprint(fuelCard.fuelCard_bp)
    app.register_blueprint(combustivel.combustivel_bp)
    app.register_blueprint(cargo.cargo_bp)
    app.register_blueprint(departamento.departamento_bp)
    app.register_blueprint(grupo.grupo_bp)
    app.register_blueprint(controlColab.controlColab_bp)

    app.run(host='localhost', port=5003, debug=True)
