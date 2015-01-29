import _oo.class.Evento
import _oo.class.Asistente



class CEvento{

    def listarAsistentes(idEvento){
        lAsistente = Asistente.query(Asistente.idEvento == idEvento)
        return lAsistente
    }
}
