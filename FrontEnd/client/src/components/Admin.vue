<template>
  <div >
    <AdminOne
      color="green--outline"
      :width="150"
      :strokeWidth="10"
    />
    <AdminTwo />
  </div>
</template>

<script>

import { ModalBus } from '../eventBus'


import AdminOne from './AdminOne'
import AdminTwo from './AdminTwo'
import Alert from './Alert'
import ModalRoot from './ModalRoot'

export default {
  name: 'Admin',
  components: {
    AdminOne,
    AdminTwo
  },

  methods: {
    openSuccessAlert () {
      ModalBus.$emit('open', {
        component: Alert,
        props: { text: 'Everything is working great!', type: 'success' }
      })
    },
    openDangerAlert () {
      const props = {
        type: 'error',
        text: 'The server returned 500 again! omg!'
      }
      ModalBus.$emit('open', { component: Alert, title: 'An error has occured', props })
    },
    openClosableInside () {
      ModalBus.$emit('open', { component: ClosableInside, title: 'Close dialog from component' })
    },
    openSignIn () {
      ModalBus.$emit('open', { component: SignInForm, title: 'New user', closeOnClick: false })
    }
  }




}
</script>
<style scoped>
.content {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center
}
</style>